from . import base_types
from ._SearchCriteria2Choice import SearchCriteria2Choice
from ._DateOrDateTimePeriod1Choice import DateOrDateTimePeriod1Choice
from ._LegalMandate1 import LegalMandate1
from ._Max35Text import Max35Text
from ._SupplementaryData1 import SupplementaryData1
from ._YesNoIndicator import YesNoIndicator
from ._DueDate1 import DueDate1

class InformationRequestOpeningV02(base_types._BaseFieldType):

	__slots__ = ["_CnfdtltySts", "_SchCrit", "_InvstgtnId", "_LglMndtBsis", "_DueDt", "_InvstgtnPrd", "_SplmtryData"]
	@property
	def CnfdtltySts(self):
		return self._CnfdtltySts

	@CnfdtltySts.setter
	def CnfdtltySts(self, value):
		self._CnfdtltySts = value if type(value) != base_types.auto else self.make_default("CnfdtltySts")

	@CnfdtltySts.deleter
	def CnfdtltySts(self):
		del self._CnfdtltySts
		self._CnfdtltySts = None

	@property
	def SchCrit(self):
		return self._SchCrit

	@SchCrit.setter
	def SchCrit(self, value):
		self._SchCrit = value if type(value) != base_types.auto else self.make_default("SchCrit")

	@SchCrit.deleter
	def SchCrit(self):
		del self._SchCrit
		self._SchCrit = None

	@property
	def InvstgtnId(self):
		return self._InvstgtnId

	@InvstgtnId.setter
	def InvstgtnId(self, value):
		self._InvstgtnId = value if type(value) != base_types.auto else self.make_default("InvstgtnId")

	@InvstgtnId.deleter
	def InvstgtnId(self):
		del self._InvstgtnId
		self._InvstgtnId = None

	@property
	def LglMndtBsis(self):
		return self._LglMndtBsis

	@LglMndtBsis.setter
	def LglMndtBsis(self, value):
		self._LglMndtBsis = value if type(value) != base_types.auto else self.make_default("LglMndtBsis")

	@LglMndtBsis.deleter
	def LglMndtBsis(self):
		del self._LglMndtBsis
		self._LglMndtBsis = None

	@property
	def DueDt(self):
		return self._DueDt

	@DueDt.setter
	def DueDt(self, value):
		self._DueDt = value if type(value) != base_types.auto else self.make_default("DueDt")

	@DueDt.deleter
	def DueDt(self):
		del self._DueDt
		self._DueDt = None

	@property
	def InvstgtnPrd(self):
		return self._InvstgtnPrd

	@InvstgtnPrd.setter
	def InvstgtnPrd(self, value):
		self._InvstgtnPrd = value if type(value) != base_types.auto else self.make_default("InvstgtnPrd")

	@InvstgtnPrd.deleter
	def InvstgtnPrd(self):
		del self._InvstgtnPrd
		self._InvstgtnPrd = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CnfdtltySts', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchCrit', type=SearchCriteria2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstgtnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglMndtBsis', type=LegalMandate1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DueDt', type=DueDate1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstgtnPrd', type=DateOrDateTimePeriod1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

