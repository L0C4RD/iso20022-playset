# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BlockChainAddressWallet5
from . import CollateralAccount3
from . import DateAndDateTime2Choice
from . import ExposureType11Code
from . import PartyIdentification178Choice
from . import PartyIdentification242

class Obligation11(base_types._BaseFieldType):

	__slots__ = ["_BlckChainAdrOrWllt", "_CollAcctId", "_PtyA", "_PtyB", "_SvcgPtyA", "_SvcgPtyB", "_ValtnDt", "_XpsrTp"]
	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if value is not None else base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', BlockChainAddressWallet5, False)

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', BlockChainAddressWallet5, False)

	@property
	def CollAcctId(self):
		return self._CollAcctId

	@CollAcctId.setter
	def CollAcctId(self, value):
		self._CollAcctId = value if value is not None else base_types.UninitialisedField(self, 'CollAcctId', CollateralAccount3, False)

	@CollAcctId.deleter
	def CollAcctId(self):
		del self._CollAcctId
		self._CollAcctId = base_types.UninitialisedField(self, 'CollAcctId', CollateralAccount3, False)

	@property
	def PtyA(self):
		return self._PtyA

	@PtyA.setter
	def PtyA(self, value):
		self._PtyA = value if value is not None else base_types.UninitialisedField(self, 'PtyA', PartyIdentification242, False)

	@PtyA.deleter
	def PtyA(self):
		del self._PtyA
		self._PtyA = base_types.UninitialisedField(self, 'PtyA', PartyIdentification242, False)

	@property
	def PtyB(self):
		return self._PtyB

	@PtyB.setter
	def PtyB(self, value):
		self._PtyB = value if value is not None else base_types.UninitialisedField(self, 'PtyB', PartyIdentification242, False)

	@PtyB.deleter
	def PtyB(self):
		del self._PtyB
		self._PtyB = base_types.UninitialisedField(self, 'PtyB', PartyIdentification242, False)

	@property
	def SvcgPtyA(self):
		return self._SvcgPtyA

	@SvcgPtyA.setter
	def SvcgPtyA(self, value):
		self._SvcgPtyA = value if value is not None else base_types.UninitialisedField(self, 'SvcgPtyA', PartyIdentification178Choice, False)

	@SvcgPtyA.deleter
	def SvcgPtyA(self):
		del self._SvcgPtyA
		self._SvcgPtyA = base_types.UninitialisedField(self, 'SvcgPtyA', PartyIdentification178Choice, False)

	@property
	def SvcgPtyB(self):
		return self._SvcgPtyB

	@SvcgPtyB.setter
	def SvcgPtyB(self, value):
		self._SvcgPtyB = value if value is not None else base_types.UninitialisedField(self, 'SvcgPtyB', PartyIdentification178Choice, False)

	@SvcgPtyB.deleter
	def SvcgPtyB(self):
		del self._SvcgPtyB
		self._SvcgPtyB = base_types.UninitialisedField(self, 'SvcgPtyB', PartyIdentification178Choice, False)

	@property
	def ValtnDt(self):
		return self._ValtnDt

	@ValtnDt.setter
	def ValtnDt(self, value):
		self._ValtnDt = value if value is not None else base_types.UninitialisedField(self, 'ValtnDt', DateAndDateTime2Choice, False)

	@ValtnDt.deleter
	def ValtnDt(self):
		del self._ValtnDt
		self._ValtnDt = base_types.UninitialisedField(self, 'ValtnDt', DateAndDateTime2Choice, False)

	@property
	def XpsrTp(self):
		return self._XpsrTp

	@XpsrTp.setter
	def XpsrTp(self, value):
		self._XpsrTp = value if value is not None else base_types.UninitialisedField(self, 'XpsrTp', ExposureType11Code, False)

	@XpsrTp.deleter
	def XpsrTp(self):
		del self._XpsrTp
		self._XpsrTp = base_types.UninitialisedField(self, 'XpsrTp', ExposureType11Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollAcctId', type=CollateralAccount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyA', type=PartyIdentification242, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyB', type=PartyIdentification242, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcgPtyA', type=PartyIdentification178Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcgPtyB', type=PartyIdentification178Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnDt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrTp', type=ExposureType11Code, min=0, max=1, mutex_group=None, array=False),
	))