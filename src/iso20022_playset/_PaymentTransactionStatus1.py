# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import StatusReasonInformation12
from . import TransactionStatus1Choice

class PaymentTransactionStatus1(base_types._BaseFieldType):

	__slots__ = ["_Sts", "_StsRsnInf"]
	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', TransactionStatus1Choice, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', TransactionStatus1Choice, False)

	@property
	def StsRsnInf(self):
		return self._StsRsnInf

	@StsRsnInf.setter
	def StsRsnInf(self, value):
		self._StsRsnInf = value if value is not None else base_types.UninitialisedField(self, 'StsRsnInf', StatusReasonInformation12, True)

	@StsRsnInf.deleter
	def StsRsnInf(self):
		del self._StsRsnInf
		self._StsRsnInf = base_types.UninitialisedField(self, 'StsRsnInf', StatusReasonInformation12, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sts', type=TransactionStatus1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsnInf', type=StatusReasonInformation12, min=0, max=None, mutex_group=None, array=True),
	))