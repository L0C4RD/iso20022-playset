# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateOrDateTimePeriod1Choice
from . import DueDate1
from . import LegalMandate1
from . import Max35Text
from . import SearchCriteria2Choice
from . import SupplementaryData1
from . import YesNoIndicator

class InformationRequestOpeningV02(base_types._BaseFieldType):

	__slots__ = ["_CnfdtltySts", "_DueDt", "_InvstgtnId", "_InvstgtnPrd", "_LglMndtBsis", "_SchCrit", "_SplmtryData"]
	@property
	def CnfdtltySts(self):
		return self._CnfdtltySts

	@CnfdtltySts.setter
	def CnfdtltySts(self, value):
		self._CnfdtltySts = value if value is not None else base_types.UninitialisedField(self, 'CnfdtltySts', YesNoIndicator, False)

	@CnfdtltySts.deleter
	def CnfdtltySts(self):
		del self._CnfdtltySts
		self._CnfdtltySts = base_types.UninitialisedField(self, 'CnfdtltySts', YesNoIndicator, False)

	@property
	def DueDt(self):
		return self._DueDt

	@DueDt.setter
	def DueDt(self, value):
		self._DueDt = value if value is not None else base_types.UninitialisedField(self, 'DueDt', DueDate1, False)

	@DueDt.deleter
	def DueDt(self):
		del self._DueDt
		self._DueDt = base_types.UninitialisedField(self, 'DueDt', DueDate1, False)

	@property
	def InvstgtnId(self):
		return self._InvstgtnId

	@InvstgtnId.setter
	def InvstgtnId(self, value):
		self._InvstgtnId = value if value is not None else base_types.UninitialisedField(self, 'InvstgtnId', Max35Text, False)

	@InvstgtnId.deleter
	def InvstgtnId(self):
		del self._InvstgtnId
		self._InvstgtnId = base_types.UninitialisedField(self, 'InvstgtnId', Max35Text, False)

	@property
	def InvstgtnPrd(self):
		return self._InvstgtnPrd

	@InvstgtnPrd.setter
	def InvstgtnPrd(self, value):
		self._InvstgtnPrd = value if value is not None else base_types.UninitialisedField(self, 'InvstgtnPrd', DateOrDateTimePeriod1Choice, False)

	@InvstgtnPrd.deleter
	def InvstgtnPrd(self):
		del self._InvstgtnPrd
		self._InvstgtnPrd = base_types.UninitialisedField(self, 'InvstgtnPrd', DateOrDateTimePeriod1Choice, False)

	@property
	def LglMndtBsis(self):
		return self._LglMndtBsis

	@LglMndtBsis.setter
	def LglMndtBsis(self, value):
		self._LglMndtBsis = value if value is not None else base_types.UninitialisedField(self, 'LglMndtBsis', LegalMandate1, False)

	@LglMndtBsis.deleter
	def LglMndtBsis(self):
		del self._LglMndtBsis
		self._LglMndtBsis = base_types.UninitialisedField(self, 'LglMndtBsis', LegalMandate1, False)

	@property
	def SchCrit(self):
		return self._SchCrit

	@SchCrit.setter
	def SchCrit(self, value):
		self._SchCrit = value if value is not None else base_types.UninitialisedField(self, 'SchCrit', SearchCriteria2Choice, False)

	@SchCrit.deleter
	def SchCrit(self):
		del self._SchCrit
		self._SchCrit = base_types.UninitialisedField(self, 'SchCrit', SearchCriteria2Choice, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CnfdtltySts', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DueDt', type=DueDate1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstgtnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstgtnPrd', type=DateOrDateTimePeriod1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglMndtBsis', type=LegalMandate1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchCrit', type=SearchCriteria2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))