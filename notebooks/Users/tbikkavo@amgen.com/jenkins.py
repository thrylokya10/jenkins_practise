# Databricks notebook source
cohort_list=spark.table("dev_mai_upgrade.cohort_list_kyprolis")
display(cohort_list)