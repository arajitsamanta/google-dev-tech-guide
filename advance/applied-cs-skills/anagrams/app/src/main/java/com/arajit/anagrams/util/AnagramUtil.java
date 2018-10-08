package com.arajit.anagrams.util;

import java.util.Arrays;

public class AnagramUtil {

    private  AnagramUtil(){}

    // Method to sort a string alphabetically
    public static String sortLetters(String inputString)
    {
        // convert input string to char array
        char tempArray[] = inputString.toCharArray();

        // sort tempArray
        Arrays.sort(tempArray);

        // return new sorted string
        return new String(tempArray);
    }
}
