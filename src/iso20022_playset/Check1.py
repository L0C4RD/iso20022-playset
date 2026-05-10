from . import base_types
import CheckType1Code
import Max35Text
import Max3Text
import TrackData2

class Check1(base_types._BaseFieldType):

	__slots__ = ["_Ctry", "_ChckTp", "_ChckTrckData2", "_BkId", "_ChckCardNb", "_ChckNb", "_AcctNb"]
	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	@property
	def ChckTp(self):
		return self._ChckTp

	@ChckTp.setter
	def ChckTp(self, value):
		self._ChckTp = value if type(value) != auto else self.make_default("ChckTp")

	@ChckTp.deleter
	def ChckTp(self):
		del self._ChckTp
		self._ChckTp = None

	@property
	def ChckTrckData2(self):
		return self._ChckTrckData2

	@ChckTrckData2.setter
	def ChckTrckData2(self, value):
		self._ChckTrckData2 = value if type(value) != auto else self.make_default("ChckTrckData2")

	@ChckTrckData2.deleter
	def ChckTrckData2(self):
		del self._ChckTrckData2
		self._ChckTrckData2 = None

	@property
	def BkId(self):
		return self._BkId

	@BkId.setter
	def BkId(self, value):
		self._BkId = value if type(value) != auto else self.make_default("BkId")

	@BkId.deleter
	def BkId(self):
		del self._BkId
		self._BkId = None

	@property
	def ChckCardNb(self):
		return self._ChckCardNb

	@ChckCardNb.setter
	def ChckCardNb(self, value):
		self._ChckCardNb = value if type(value) != auto else self.make_default("ChckCardNb")

	@ChckCardNb.deleter
	def ChckCardNb(self):
		del self._ChckCardNb
		self._ChckCardNb = None

	@property
	def ChckNb(self):
		return self._ChckNb

	@ChckNb.setter
	def ChckNb(self, value):
		self._ChckNb = value if type(value) != auto else self.make_default("ChckNb")

	@ChckNb.deleter
	def ChckNb(self):
		del self._ChckNb
		self._ChckNb = None

	@property
	def AcctNb(self):
		return self._AcctNb

	@AcctNb.setter
	def AcctNb(self, value):
		self._AcctNb = value if type(value) != auto else self.make_default("AcctNb")

	@AcctNb.deleter
	def AcctNb(self):
		del self._AcctNb
		self._AcctNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctry', type=Max3Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckTp', type=CheckType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckTrckData2', type=TrackData2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BkId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckCardNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

