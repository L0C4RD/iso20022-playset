from . import base_types
import ISODate
import CorporateActionOption1FormatChoice
import YesNoIndicator
import PartyIdentification2Choice
import Exact3NumericText
import UnitOrFaceAmount1Choice
import Max35Text
import DistributionInstructionType1Code

class CorporateActionMovement1(base_types._BaseFieldType):

	__slots__ = ["_ReqdExctnDt", "_OrdrTp", "_AcctOwnrId", "_OptnNb", "_OptnTp", "_AcctId", "_ConfdBalSctiesQty", "_HghPrtyInd"]
	@property
	def ReqdExctnDt(self):
		return self._ReqdExctnDt

	@ReqdExctnDt.setter
	def ReqdExctnDt(self, value):
		self._ReqdExctnDt = value if type(value) != auto else self.make_default("ReqdExctnDt")

	@ReqdExctnDt.deleter
	def ReqdExctnDt(self):
		del self._ReqdExctnDt
		self._ReqdExctnDt = None

	@property
	def OrdrTp(self):
		return self._OrdrTp

	@OrdrTp.setter
	def OrdrTp(self, value):
		self._OrdrTp = value if type(value) != auto else self.make_default("OrdrTp")

	@OrdrTp.deleter
	def OrdrTp(self):
		del self._OrdrTp
		self._OrdrTp = None

	@property
	def AcctOwnrId(self):
		return self._AcctOwnrId

	@AcctOwnrId.setter
	def AcctOwnrId(self, value):
		self._AcctOwnrId = value if type(value) != auto else self.make_default("AcctOwnrId")

	@AcctOwnrId.deleter
	def AcctOwnrId(self):
		del self._AcctOwnrId
		self._AcctOwnrId = None

	@property
	def OptnNb(self):
		return self._OptnNb

	@OptnNb.setter
	def OptnNb(self, value):
		self._OptnNb = value if type(value) != auto else self.make_default("OptnNb")

	@OptnNb.deleter
	def OptnNb(self):
		del self._OptnNb
		self._OptnNb = None

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if type(value) != auto else self.make_default("OptnTp")

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = None

	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	@property
	def ConfdBalSctiesQty(self):
		return self._ConfdBalSctiesQty

	@ConfdBalSctiesQty.setter
	def ConfdBalSctiesQty(self, value):
		self._ConfdBalSctiesQty = value if type(value) != auto else self.make_default("ConfdBalSctiesQty")

	@ConfdBalSctiesQty.deleter
	def ConfdBalSctiesQty(self):
		del self._ConfdBalSctiesQty
		self._ConfdBalSctiesQty = None

	@property
	def HghPrtyInd(self):
		return self._HghPrtyInd

	@HghPrtyInd.setter
	def HghPrtyInd(self, value):
		self._HghPrtyInd = value if type(value) != auto else self.make_default("HghPrtyInd")

	@HghPrtyInd.deleter
	def HghPrtyInd(self):
		del self._HghPrtyInd
		self._HghPrtyInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ReqdExctnDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrTp', type=DistributionInstructionType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnrId', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnNb', type=Exact3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfdBalSctiesQty', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HghPrtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))

