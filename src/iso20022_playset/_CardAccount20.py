# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountChoiceMethod1Code
from . import AccountIdentification80Choice
from . import ActiveCurrencyCode
from . import CardAccountType3Code
from . import Max70Text
from . import NameAndAddress3
from . import PartyIdentification177Choice

class CardAccount20(base_types._BaseFieldType):

	__slots__ = ["_AcctIdr", "_AcctNm", "_AcctOwnr", "_Ccy", "_SelctdAcctTp", "_SelctnMtd", "_Svcr"]
	@property
	def AcctIdr(self):
		return self._AcctIdr

	@AcctIdr.setter
	def AcctIdr(self, value):
		self._AcctIdr = value if value is not None else base_types.UninitialisedField(self, 'AcctIdr', AccountIdentification80Choice, False)

	@AcctIdr.deleter
	def AcctIdr(self):
		del self._AcctIdr
		self._AcctIdr = base_types.UninitialisedField(self, 'AcctIdr', AccountIdentification80Choice, False)

	@property
	def AcctNm(self):
		return self._AcctNm

	@AcctNm.setter
	def AcctNm(self, value):
		self._AcctNm = value if value is not None else base_types.UninitialisedField(self, 'AcctNm', Max70Text, False)

	@AcctNm.deleter
	def AcctNm(self):
		del self._AcctNm
		self._AcctNm = base_types.UninitialisedField(self, 'AcctNm', Max70Text, False)

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', NameAndAddress3, False)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', NameAndAddress3, False)

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@property
	def SelctdAcctTp(self):
		return self._SelctdAcctTp

	@SelctdAcctTp.setter
	def SelctdAcctTp(self, value):
		self._SelctdAcctTp = value if value is not None else base_types.UninitialisedField(self, 'SelctdAcctTp', CardAccountType3Code, False)

	@SelctdAcctTp.deleter
	def SelctdAcctTp(self):
		del self._SelctdAcctTp
		self._SelctdAcctTp = base_types.UninitialisedField(self, 'SelctdAcctTp', CardAccountType3Code, False)

	@property
	def SelctnMtd(self):
		return self._SelctnMtd

	@SelctnMtd.setter
	def SelctnMtd(self, value):
		self._SelctnMtd = value if value is not None else base_types.UninitialisedField(self, 'SelctnMtd', AccountChoiceMethod1Code, False)

	@SelctnMtd.deleter
	def SelctnMtd(self):
		del self._SelctnMtd
		self._SelctnMtd = base_types.UninitialisedField(self, 'SelctnMtd', AccountChoiceMethod1Code, False)

	@property
	def Svcr(self):
		return self._Svcr

	@Svcr.setter
	def Svcr(self, value):
		self._Svcr = value if value is not None else base_types.UninitialisedField(self, 'Svcr', PartyIdentification177Choice, False)

	@Svcr.deleter
	def Svcr(self):
		del self._Svcr
		self._Svcr = base_types.UninitialisedField(self, 'Svcr', PartyIdentification177Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctIdr', type=AccountIdentification80Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=NameAndAddress3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SelctdAcctTp', type=CardAccountType3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SelctnMtd', type=AccountChoiceMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Svcr', type=PartyIdentification177Choice, min=0, max=1, mutex_group=None, array=False),
	))