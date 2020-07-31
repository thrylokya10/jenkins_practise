# Databricks notebook source
cohort_list_1=spark.table("dev_mai_upgrade.cohort_list_kyprolis")
display(cohort_list_1)