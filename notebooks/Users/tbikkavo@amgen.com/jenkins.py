# Databricks notebook source
list_last=spark.table("dev_mai_upgrade.cohort_list_kyprolis")
display(list_last)