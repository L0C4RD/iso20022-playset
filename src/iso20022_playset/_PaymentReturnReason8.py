# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BankTransactionCodeStructure4
from . import Max105Text
from . import PartyIdentification272
from . import ReturnReason5Choice

class PaymentReturnReason8(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_OrgnlBkTxCd", "_Orgtr", "_Rsn"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max105Text, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max105Text, True)

	@property
	def OrgnlBkTxCd(self):
		return self._OrgnlBkTxCd

	@OrgnlBkTxCd.setter
	def OrgnlBkTxCd(self, value):
		self._OrgnlBkTxCd = value if value is not None else base_types.UninitialisedField(self, 'OrgnlBkTxCd', BankTransactionCodeStructure4, False)

	@OrgnlBkTxCd.deleter
	def OrgnlBkTxCd(self):
		del self._OrgnlBkTxCd
		self._OrgnlBkTxCd = base_types.UninitialisedField(self, 'OrgnlBkTxCd', BankTransactionCodeStructure4, False)

	@property
	def Orgtr(self):
		return self._Orgtr

	@Orgtr.setter
	def Orgtr(self, value):
		self._Orgtr = value if value is not None else base_types.UninitialisedField(self, 'Orgtr', PartyIdentification272, False)

	@Orgtr.deleter
	def Orgtr(self):
		del self._Orgtr
		self._Orgtr = base_types.UninitialisedField(self, 'Orgtr', PartyIdentification272, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', ReturnReason5Choice, False)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', ReturnReason5Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max105Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlBkTxCd', type=BankTransactionCodeStructure4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Orgtr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=ReturnReason5Choice, min=0, max=1, mutex_group=None, array=False),
	))