# Databricks notebook source
sunday=spark.table("dev_mai_upgrade.cohort_list_kyprolis")
display(sunday)