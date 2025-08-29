import java.util.Scanner;
public class ScoreSheetApp {
	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		System.out.print("Enter number of students: ");
		int studentCount = scanner.nextInt();

		System.out.print("Enter number of subjects: ");
		int subjectCount = scanner.nextInt();

		String[] students = new String[studentCount];
		int[][] scores = new int[studentCount][subjectCount];
		int[] totals = new int[studentCount];
		double[] averages = new double[studentCount];

		for (int count = 0; count < studentCount; count++) {
			System.out.println("Entering scores for Student " + (count + 1) + ":");

		for (int counter = 0; counter < subjectCount; counter++) {
			System.out.print("Enter score for Subject " + (counter + 1) + ": ");
			scores[count][counter] = scanner.nextInt();
			totals[count] += scores[count][counter];
			subjectTotals[counter] += scores[count][counter];
            }
            averages[count] = (double) totals[count] / subjectCount;
        }