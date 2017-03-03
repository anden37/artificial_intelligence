package model;

import java.util.LinkedList;

public class MatrixCreator {
	private int rows, cols, nDirections;
	private double[][] transitionMatrix;

	public MatrixCreator(int rows, int cols, int nDirections) {
		this.rows = rows;
		this.cols = cols;
		this.nDirections = nDirections;
		createTransitionMatrix();
//		createObservationMatrix();
	}

	private void createTransitionMatrix() {
		transitionMatrix = new double[rows*cols*nDirections][rows*cols*nDirections];
		for (int state = 0; state < rows * cols * nDirections; state++) {
			for (int row = 0; row < rows; row++) {
				for (int col = 0; col < cols; col++) {
					for (int direction = 0; direction < nDirections; direction++) {
						distributeProbability(row, col, direction);
					}
				}
			}
		}
	}
	
	public void printTransitionMatrix() {
		for (int row=0; row < rows*cols*nDirections; row++) {
			for (int col=0; col < rows*cols*nDirections; col++) {
				System.out.print(transitionMatrix[row][col] + " ");
			}
			System.out.println();
		}
	}
	
	private void distributeProbability(int row, int col, int direction) {
		State currState = new State(row, col, direction);
		State nextState = getNextState(row, col, direction);
		double pointDistribution = getLeftovers(currState, nextState);
		LinkedList<State> alternativeNextStates = getAltStates(currState);
		double nGoodTransitions = (double) alternativeNextStates.size();
		for (State s : alternativeNextStates) {
			setTransitionProb(currState, s, pointDistribution / nGoodTransitions);
		}
	}
	
	private LinkedList<State> getAltStates(State currState) {
		LinkedList<State> states = new LinkedList<State>();
		int currDirection = currState.getDirection();
		for (int dir=0; dir < nDirections; dir++) {
			State nextState = getNextState(currState.getRow(), currState.getCol(), dir);
			if (stateExists(nextState) && (dir != currDirection)) {
				states.add(nextState);
			}
		}
		return states;
	}
	
	private State getNextState(int row, int col, int direction) {
		switch (direction){
			case 0:
				return new State(row, col-1, direction);
			case 1:
				return new State(row-1, col, direction);
			case 2:
				return new State(row, col+1, direction);
			case 3:
				return new State(row+1, col, direction);
			default:
				return new State(-1, -1, -1);
		}
	}
	
	private double getLeftovers(State currState, State nextState) {
		if (!stateExists(nextState)) {
			return 1.0;
		}
		setTransitionProb(currState, nextState, 0.7);
		return 0.3;
	}
	
	private boolean stateExists(State state) {
		int row = state.getRow();
		int col = state.getCol();
		if ((row >= 0 && row < rows) && (col >= 0 && col < cols)) {
			return true;
		}
		return false;
	}
	
	private void setTransitionProb(State currState, State nextState, double probability) {
		int currStateIdx = getStateIdx(currState);
		int nextStateIdx = getStateIdx(nextState);
		transitionMatrix[currStateIdx][nextStateIdx] = probability;
	}
	
	private int getStateIdx(State state) {
		int row = state.getRow();
		int col = state.getCol();
		int dir = state.getDirection();
		return col*nDirections + dir + row*cols*nDirections;
	}
	
	public static void main(String[] args) {
		MatrixCreator mc = new MatrixCreator(5, 5, 4);
		mc.printTransitionMatrix();
	}
}
