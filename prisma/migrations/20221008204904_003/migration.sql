/*
  Warnings:

  - You are about to drop the column `message` on the `Traffic` table. All the data in the column will be lost.
  - You are about to drop the column `start` on the `Traffic` table. All the data in the column will be lost.
  - You are about to drop the column `stop` on the `Traffic` table. All the data in the column will be lost.
  - You are about to drop the column `zipcode` on the `Traffic` table. All the data in the column will be lost.
  - A unique constraint covering the columns `[id]` on the table `User` will be added. If there are existing duplicate values, this will fail.
  - Added the required column `description` to the `Traffic` table without a default value. This is not possible if the table is not empty.
  - Added the required column `state` to the `Traffic` table without a default value. This is not possible if the table is not empty.
  - Added the required column `status` to the `Traffic` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "Traffic" DROP COLUMN "message",
DROP COLUMN "start",
DROP COLUMN "stop",
DROP COLUMN "zipcode",
ADD COLUMN     "active" BOOLEAN NOT NULL DEFAULT true,
ADD COLUMN     "date" TIMESTAMP(3),
ADD COLUMN     "description" TEXT NOT NULL,
ADD COLUMN     "state" TEXT NOT NULL,
ADD COLUMN     "status" TEXT NOT NULL,
ADD COLUMN     "time" TIMESTAMP(3);

-- CreateTable
CREATE TABLE "Points" (
    "id" SERIAL NOT NULL,
    "points" DECIMAL(65,30) NOT NULL DEFAULT 0.00,
    "userId" INTEGER NOT NULL,

    CONSTRAINT "Points_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "Points_userId_key" ON "Points"("userId");

-- CreateIndex
CREATE UNIQUE INDEX "User_id_key" ON "User"("id");

-- AddForeignKey
ALTER TABLE "Points" ADD CONSTRAINT "Points_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
