# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification4Choice
from . import ActiveCurrencyAndAmount
from . import PartyIdentificationAndAccount31

class Contribution1(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_IncrCvrgAmt", "_NonClrMmb", "_ReqrdAmt"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if value is not None else base_types.UninitialisedField(self, 'Acct', AccountIdentification4Choice, False)

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = base_types.UninitialisedField(self, 'Acct', AccountIdentification4Choice, False)

	@property
	def IncrCvrgAmt(self):
		return self._IncrCvrgAmt

	@IncrCvrgAmt.setter
	def IncrCvrgAmt(self, value):
		self._IncrCvrgAmt = value if value is not None else base_types.UninitialisedField(self, 'IncrCvrgAmt', ActiveCurrencyAndAmount, False)

	@IncrCvrgAmt.deleter
	def IncrCvrgAmt(self):
		del self._IncrCvrgAmt
		self._IncrCvrgAmt = base_types.UninitialisedField(self, 'IncrCvrgAmt', ActiveCurrencyAndAmount, False)

	@property
	def NonClrMmb(self):
		return self._NonClrMmb

	@NonClrMmb.setter
	def NonClrMmb(self, value):
		self._NonClrMmb = value if value is not None else base_types.UninitialisedField(self, 'NonClrMmb', PartyIdentificationAndAccount31, False)

	@NonClrMmb.deleter
	def NonClrMmb(self):
		del self._NonClrMmb
		self._NonClrMmb = base_types.UninitialisedField(self, 'NonClrMmb', PartyIdentificationAndAccount31, False)

	@property
	def ReqrdAmt(self):
		return self._ReqrdAmt

	@ReqrdAmt.setter
	def ReqrdAmt(self, value):
		self._ReqrdAmt = value if value is not None else base_types.UninitialisedField(self, 'ReqrdAmt', ActiveCurrencyAndAmount, False)

	@ReqrdAmt.deleter
	def ReqrdAmt(self):
		del self._ReqrdAmt
		self._ReqrdAmt = base_types.UninitialisedField(self, 'ReqrdAmt', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=AccountIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncrCvrgAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonClrMmb', type=PartyIdentificationAndAccount31, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqrdAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))