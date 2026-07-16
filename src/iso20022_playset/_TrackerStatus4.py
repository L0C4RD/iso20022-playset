# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountConsistencyType1Code
from . import DateAndDateTime2Choice
from . import ExternalPaymentTransactionStatus1Code
from . import PaymentRejectReturnReason1
from . import PaymentStatusReason1

class TrackerStatus4(base_types._BaseFieldType):

	__slots__ = ["_AmtIncnsstncy", "_Dt", "_RjctRtrRsn", "_Sts", "_StsRsn"]
	@property
	def AmtIncnsstncy(self):
		return self._AmtIncnsstncy

	@AmtIncnsstncy.setter
	def AmtIncnsstncy(self, value):
		self._AmtIncnsstncy = value if value is not None else base_types.UninitialisedField(self, 'AmtIncnsstncy', AmountConsistencyType1Code, False)

	@AmtIncnsstncy.deleter
	def AmtIncnsstncy(self):
		del self._AmtIncnsstncy
		self._AmtIncnsstncy = base_types.UninitialisedField(self, 'AmtIncnsstncy', AmountConsistencyType1Code, False)

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', DateAndDateTime2Choice, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', DateAndDateTime2Choice, False)

	@property
	def RjctRtrRsn(self):
		return self._RjctRtrRsn

	@RjctRtrRsn.setter
	def RjctRtrRsn(self, value):
		self._RjctRtrRsn = value if value is not None else base_types.UninitialisedField(self, 'RjctRtrRsn', PaymentRejectReturnReason1, True)

	@RjctRtrRsn.deleter
	def RjctRtrRsn(self):
		del self._RjctRtrRsn
		self._RjctRtrRsn = base_types.UninitialisedField(self, 'RjctRtrRsn', PaymentRejectReturnReason1, True)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', ExternalPaymentTransactionStatus1Code, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', ExternalPaymentTransactionStatus1Code, False)

	@property
	def StsRsn(self):
		return self._StsRsn

	@StsRsn.setter
	def StsRsn(self, value):
		self._StsRsn = value if value is not None else base_types.UninitialisedField(self, 'StsRsn', PaymentStatusReason1, True)

	@StsRsn.deleter
	def StsRsn(self):
		del self._StsRsn
		self._StsRsn = base_types.UninitialisedField(self, 'StsRsn', PaymentStatusReason1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtIncnsstncy', type=AmountConsistencyType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctRtrRsn', type=PaymentRejectReturnReason1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=ExternalPaymentTransactionStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsn', type=PaymentStatusReason1, min=0, max=None, mutex_group=None, array=True),
	))