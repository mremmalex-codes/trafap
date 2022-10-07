/*
  Warnings:

  - You are about to drop the `Blog` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE "Blog" DROP CONSTRAINT "Blog_userId_fkey";

-- DropTable
DROP TABLE "Blog";

-- CreateTable
CREATE TABLE "Traffic" (
    "id" SERIAL NOT NULL,
    "location" TEXT NOT NULL,
    "message" TEXT NOT NULL,
    "start" TIMESTAMP(3) NOT NULL,
    "stop" TIMESTAMP(3) NOT NULL,
    "zipcode" INTEGER NOT NULL,
    "create_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "update_at" TIMESTAMP(3) NOT NULL,
    "userId" INTEGER,

    CONSTRAINT "Traffic_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "Traffic" ADD CONSTRAINT "Traffic_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE SET NULL ON UPDATE CASCADE;
