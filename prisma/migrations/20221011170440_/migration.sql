-- DropForeignKey
ALTER TABLE "Points" DROP CONSTRAINT "Points_userId_fkey";

-- DropForeignKey
ALTER TABLE "Traffic" DROP CONSTRAINT "Traffic_userId_fkey";

-- AddForeignKey
ALTER TABLE "Traffic" ADD CONSTRAINT "Traffic_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Points" ADD CONSTRAINT "Points_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;
