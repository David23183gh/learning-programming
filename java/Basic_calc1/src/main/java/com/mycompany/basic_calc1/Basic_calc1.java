/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.basic_calc1;

import java.util.Scanner;

public class Basic_calc1 {

    public static void main(String[] args) {
        float num1=0, num2=0, add=0 ;
        int opt=0;
       
        Scanner scanner = new Scanner(System.in);
        System.out.println("...My basic calc... ");
        
        System.out.println("enter first number: ");
        num1 = scanner.nextFloat ();
        
        System.out.println("enter second number: ");
        num2 = scanner.nextFloat ();
        
        System.out.println(""
            + "[1]. Addition\n"
            + "[2]. Substraction\n"
            + "[3]. multiplication\n"
            + "[4]. Division\n"
            + "[5]. Average\n"
            + ".::: Enter any option: ");  
        
        opt = scanner.nextInt();
        
        if (opt==1)
            System.out.println("Addition is:" + (num1 + num2));
        if (opt==2)
            System.out.println("Substraction is:" + (num1 - num2));
        if (opt==3)
            System.out.println("Multiplication is:" + (num1 * num2));
        if (opt==4)
            System.out.println("Divition is:" + (num1 / num2));
        if (opt==5)
            System.out.println("Average is:" + (num1 + num2)/2);
        else
            System.out.println("error");
    }
}