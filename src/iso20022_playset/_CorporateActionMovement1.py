# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionOption1FormatChoice
from . import DistributionInstructionType1Code
from . import Exact3NumericText
from . import ISODate
from . import Max35Text
from . import PartyIdentification2Choice
from . import UnitOrFaceAmount1Choice
from . import YesNoIndicator

class CorporateActionMovement1(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_AcctOwnrId", "_ConfdBalSctiesQty", "_HghPrtyInd", "_OptnNb", "_OptnTp", "_OrdrTp", "_ReqdExctnDt"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', Max35Text, False)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', Max35Text, False)

	@property
	def AcctOwnrId(self):
		return self._AcctOwnrId

	@AcctOwnrId.setter
	def AcctOwnrId(self, value):
		self._AcctOwnrId = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnrId', PartyIdentification2Choice, False)

	@AcctOwnrId.deleter
	def AcctOwnrId(self):
		del self._AcctOwnrId
		self._AcctOwnrId = base_types.UninitialisedField(self, 'AcctOwnrId', PartyIdentification2Choice, False)

	@property
	def ConfdBalSctiesQty(self):
		return self._ConfdBalSctiesQty

	@ConfdBalSctiesQty.setter
	def ConfdBalSctiesQty(self, value):
		self._ConfdBalSctiesQty = value if value is not None else base_types.UninitialisedField(self, 'ConfdBalSctiesQty', UnitOrFaceAmount1Choice, False)

	@ConfdBalSctiesQty.deleter
	def ConfdBalSctiesQty(self):
		del self._ConfdBalSctiesQty
		self._ConfdBalSctiesQty = base_types.UninitialisedField(self, 'ConfdBalSctiesQty', UnitOrFaceAmount1Choice, False)

	@property
	def HghPrtyInd(self):
		return self._HghPrtyInd

	@HghPrtyInd.setter
	def HghPrtyInd(self, value):
		self._HghPrtyInd = value if value is not None else base_types.UninitialisedField(self, 'HghPrtyInd', YesNoIndicator, False)

	@HghPrtyInd.deleter
	def HghPrtyInd(self):
		del self._HghPrtyInd
		self._HghPrtyInd = base_types.UninitialisedField(self, 'HghPrtyInd', YesNoIndicator, False)

	@property
	def OptnNb(self):
		return self._OptnNb

	@OptnNb.setter
	def OptnNb(self, value):
		self._OptnNb = value if value is not None else base_types.UninitialisedField(self, 'OptnNb', Exact3NumericText, False)

	@OptnNb.deleter
	def OptnNb(self):
		del self._OptnNb
		self._OptnNb = base_types.UninitialisedField(self, 'OptnNb', Exact3NumericText, False)

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if value is not None else base_types.UninitialisedField(self, 'OptnTp', CorporateActionOption1FormatChoice, False)

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = base_types.UninitialisedField(self, 'OptnTp', CorporateActionOption1FormatChoice, False)

	@property
	def OrdrTp(self):
		return self._OrdrTp

	@OrdrTp.setter
	def OrdrTp(self, value):
		self._OrdrTp = value if value is not None else base_types.UninitialisedField(self, 'OrdrTp', DistributionInstructionType1Code, False)

	@OrdrTp.deleter
	def OrdrTp(self):
		del self._OrdrTp
		self._OrdrTp = base_types.UninitialisedField(self, 'OrdrTp', DistributionInstructionType1Code, False)

	@property
	def ReqdExctnDt(self):
		return self._ReqdExctnDt

	@ReqdExctnDt.setter
	def ReqdExctnDt(self, value):
		self._ReqdExctnDt = value if value is not None else base_types.UninitialisedField(self, 'ReqdExctnDt', ISODate, False)

	@ReqdExctnDt.deleter
	def ReqdExctnDt(self):
		del self._ReqdExctnDt
		self._ReqdExctnDt = base_types.UninitialisedField(self, 'ReqdExctnDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnrId', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfdBalSctiesQty', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HghPrtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnNb', type=Exact3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrTp', type=DistributionInstructionType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdExctnDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))