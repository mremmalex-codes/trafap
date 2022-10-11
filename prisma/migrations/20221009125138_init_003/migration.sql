/*
  Warnings:

  - You are about to drop the column `time` on the `Traffic` table. All the data in the column will be lost.
  - Made the column `date` on table `Traffic` required. This step will fail if there are existing NULL values in that column.

*/
-- AlterTable
ALTER TABLE "Traffic" DROP COLUMN "time",
ALTER COLUMN "date" SET NOT NULL;
