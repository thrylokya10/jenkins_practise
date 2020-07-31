# Databricks notebook source
cohort_list_new_thrylokya=spark.table("dev_mai_upgrade.cohort_list_kyprolis")
display(cohort_list_new_thrylokya)