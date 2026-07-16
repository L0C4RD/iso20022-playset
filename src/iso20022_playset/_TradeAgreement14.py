# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Exact4AlphaNumericText
from . import ISODate
from . import Max35Text
from . import Max4Text
from . import YesNoIndicator

class TradeAgreement14(base_types._BaseFieldType):

	__slots__ = ["_CmonRef", "_OprScp", "_OprTp", "_OrgtrRef", "_PdctTp", "_PmtVrssPmtInd", "_SttlmSsnIdr", "_TradDt"]
	@property
	def CmonRef(self):
		return self._CmonRef

	@CmonRef.setter
	def CmonRef(self, value):
		self._CmonRef = value if value is not None else base_types.UninitialisedField(self, 'CmonRef', Max35Text, False)

	@CmonRef.deleter
	def CmonRef(self):
		del self._CmonRef
		self._CmonRef = base_types.UninitialisedField(self, 'CmonRef', Max35Text, False)

	@property
	def OprScp(self):
		return self._OprScp

	@OprScp.setter
	def OprScp(self, value):
		self._OprScp = value if value is not None else base_types.UninitialisedField(self, 'OprScp', Max4Text, False)

	@OprScp.deleter
	def OprScp(self):
		del self._OprScp
		self._OprScp = base_types.UninitialisedField(self, 'OprScp', Max4Text, False)

	@property
	def OprTp(self):
		return self._OprTp

	@OprTp.setter
	def OprTp(self, value):
		self._OprTp = value if value is not None else base_types.UninitialisedField(self, 'OprTp', Max4Text, False)

	@OprTp.deleter
	def OprTp(self):
		del self._OprTp
		self._OprTp = base_types.UninitialisedField(self, 'OprTp', Max4Text, False)

	@property
	def OrgtrRef(self):
		return self._OrgtrRef

	@OrgtrRef.setter
	def OrgtrRef(self, value):
		self._OrgtrRef = value if value is not None else base_types.UninitialisedField(self, 'OrgtrRef', Max35Text, False)

	@OrgtrRef.deleter
	def OrgtrRef(self):
		del self._OrgtrRef
		self._OrgtrRef = base_types.UninitialisedField(self, 'OrgtrRef', Max35Text, False)

	@property
	def PdctTp(self):
		return self._PdctTp

	@PdctTp.setter
	def PdctTp(self, value):
		self._PdctTp = value if value is not None else base_types.UninitialisedField(self, 'PdctTp', Max35Text, False)

	@PdctTp.deleter
	def PdctTp(self):
		del self._PdctTp
		self._PdctTp = base_types.UninitialisedField(self, 'PdctTp', Max35Text, False)

	@property
	def PmtVrssPmtInd(self):
		return self._PmtVrssPmtInd

	@PmtVrssPmtInd.setter
	def PmtVrssPmtInd(self, value):
		self._PmtVrssPmtInd = value if value is not None else base_types.UninitialisedField(self, 'PmtVrssPmtInd', YesNoIndicator, False)

	@PmtVrssPmtInd.deleter
	def PmtVrssPmtInd(self):
		del self._PmtVrssPmtInd
		self._PmtVrssPmtInd = base_types.UninitialisedField(self, 'PmtVrssPmtInd', YesNoIndicator, False)

	@property
	def SttlmSsnIdr(self):
		return self._SttlmSsnIdr

	@SttlmSsnIdr.setter
	def SttlmSsnIdr(self, value):
		self._SttlmSsnIdr = value if value is not None else base_types.UninitialisedField(self, 'SttlmSsnIdr', Exact4AlphaNumericText, False)

	@SttlmSsnIdr.deleter
	def SttlmSsnIdr(self):
		del self._SttlmSsnIdr
		self._SttlmSsnIdr = base_types.UninitialisedField(self, 'SttlmSsnIdr', Exact4AlphaNumericText, False)

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if value is not None else base_types.UninitialisedField(self, 'TradDt', ISODate, False)

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = base_types.UninitialisedField(self, 'TradDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmonRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OprScp', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OprTp', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgtrRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtVrssPmtInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSsnIdr', type=Exact4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))