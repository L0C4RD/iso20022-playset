# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CheckType1Code
from . import Max35Text
from . import Max3Text
from . import TrackData2

class Check1(base_types._BaseFieldType):

	__slots__ = ["_AcctNb", "_BkId", "_ChckCardNb", "_ChckNb", "_ChckTp", "_ChckTrckData2", "_Ctry"]
	@property
	def AcctNb(self):
		return self._AcctNb

	@AcctNb.setter
	def AcctNb(self, value):
		self._AcctNb = value if value is not None else base_types.UninitialisedField(self, 'AcctNb', Max35Text, False)

	@AcctNb.deleter
	def AcctNb(self):
		del self._AcctNb
		self._AcctNb = base_types.UninitialisedField(self, 'AcctNb', Max35Text, False)

	@property
	def BkId(self):
		return self._BkId

	@BkId.setter
	def BkId(self, value):
		self._BkId = value if value is not None else base_types.UninitialisedField(self, 'BkId', Max35Text, False)

	@BkId.deleter
	def BkId(self):
		del self._BkId
		self._BkId = base_types.UninitialisedField(self, 'BkId', Max35Text, False)

	@property
	def ChckCardNb(self):
		return self._ChckCardNb

	@ChckCardNb.setter
	def ChckCardNb(self, value):
		self._ChckCardNb = value if value is not None else base_types.UninitialisedField(self, 'ChckCardNb', Max35Text, False)

	@ChckCardNb.deleter
	def ChckCardNb(self):
		del self._ChckCardNb
		self._ChckCardNb = base_types.UninitialisedField(self, 'ChckCardNb', Max35Text, False)

	@property
	def ChckNb(self):
		return self._ChckNb

	@ChckNb.setter
	def ChckNb(self, value):
		self._ChckNb = value if value is not None else base_types.UninitialisedField(self, 'ChckNb', Max35Text, False)

	@ChckNb.deleter
	def ChckNb(self):
		del self._ChckNb
		self._ChckNb = base_types.UninitialisedField(self, 'ChckNb', Max35Text, False)

	@property
	def ChckTp(self):
		return self._ChckTp

	@ChckTp.setter
	def ChckTp(self, value):
		self._ChckTp = value if value is not None else base_types.UninitialisedField(self, 'ChckTp', CheckType1Code, False)

	@ChckTp.deleter
	def ChckTp(self):
		del self._ChckTp
		self._ChckTp = base_types.UninitialisedField(self, 'ChckTp', CheckType1Code, False)

	@property
	def ChckTrckData2(self):
		return self._ChckTrckData2

	@ChckTrckData2.setter
	def ChckTrckData2(self, value):
		self._ChckTrckData2 = value if value is not None else base_types.UninitialisedField(self, 'ChckTrckData2', TrackData2, False)

	@ChckTrckData2.deleter
	def ChckTrckData2(self):
		del self._ChckTrckData2
		self._ChckTrckData2 = base_types.UninitialisedField(self, 'ChckTrckData2', TrackData2, False)

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if value is not None else base_types.UninitialisedField(self, 'Ctry', Max3Text, False)

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = base_types.UninitialisedField(self, 'Ctry', Max3Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BkId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckCardNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckTp', type=CheckType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckTrckData2', type=TrackData2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=Max3Text, min=0, max=1, mutex_group=None, array=False),
	))