#!/usr/bin/node
/**
 * Create a job
 */
import { createQueue } from 'kue';

const queue = createQueue();

const data = {
  phoneNumber: '+2348105347918',
  message: 'Sensei is a great programmer',
}

const job = queue
  .create('push_notification_code', data)
  .save((err) => {
    if (!err) console.log(`Notification job created: ${job.id}`);
  });

job.on('complete', (result) => {
  console.log('Notification job completed');
});

job.on('failed', (err) => { 
  console.log('Notification job failed');
});

