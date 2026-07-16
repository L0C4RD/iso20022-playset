# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionEventAndBalance28
from . import Max140Text
from . import Max35Text
from . import PartyIdentification127Choice
from . import SafekeepingPlaceFormat42Choice

class AccountIdentification77(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_BlckChainAdrOrWllt", "_CorpActnEvtAndBal", "_SfkpgAcct", "_SfkpgPlc"]
	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification127Choice, False)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification127Choice, False)

	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if value is not None else base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', Max140Text, False)

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', Max140Text, False)

	@property
	def CorpActnEvtAndBal(self):
		return self._CorpActnEvtAndBal

	@CorpActnEvtAndBal.setter
	def CorpActnEvtAndBal(self, value):
		self._CorpActnEvtAndBal = value if value is not None else base_types.UninitialisedField(self, 'CorpActnEvtAndBal', CorporateActionEventAndBalance28, True)

	@CorpActnEvtAndBal.deleter
	def CorpActnEvtAndBal(self):
		del self._CorpActnEvtAndBal
		self._CorpActnEvtAndBal = base_types.UninitialisedField(self, 'CorpActnEvtAndBal', CorporateActionEventAndBalance28, True)

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if value is not None else base_types.UninitialisedField(self, 'SfkpgAcct', Max35Text, False)

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = base_types.UninitialisedField(self, 'SfkpgAcct', Max35Text, False)

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if value is not None else base_types.UninitialisedField(self, 'SfkpgPlc', SafekeepingPlaceFormat42Choice, False)

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = base_types.UninitialisedField(self, 'SfkpgPlc', SafekeepingPlaceFormat42Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification127Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnEvtAndBal', type=CorporateActionEventAndBalance28, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SfkpgAcct', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafekeepingPlaceFormat42Choice, min=0, max=1, mutex_group=None, array=False),
	))