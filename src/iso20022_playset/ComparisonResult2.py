from . import base_types
from .Max35Text import Max35Text
from .Addition2 import Addition2
from .Replacement2 import Replacement2
from .Number import Number
from .Max350Text import Max350Text
from .Deletion2 import Deletion2

class ComparisonResult2(base_types._BaseFieldType):

	__slots__ = ["_ElmtNm", "_ElmtPth", "_Rplcmnt", "_Deltn", "_ElmtSeqNb", "_Addtn"]
	@property
	def ElmtNm(self):
		return self._ElmtNm

	@ElmtNm.setter
	def ElmtNm(self, value):
		self._ElmtNm = value if type(value) != auto else self.make_default("ElmtNm")

	@ElmtNm.deleter
	def ElmtNm(self):
		del self._ElmtNm
		self._ElmtNm = None

	@property
	def ElmtPth(self):
		return self._ElmtPth

	@ElmtPth.setter
	def ElmtPth(self, value):
		self._ElmtPth = value if type(value) != auto else self.make_default("ElmtPth")

	@ElmtPth.deleter
	def ElmtPth(self):
		del self._ElmtPth
		self._ElmtPth = None

	@property
	def Rplcmnt(self):
		return self._Rplcmnt

	@Rplcmnt.setter
	def Rplcmnt(self, value):
		self._Rplcmnt = value if type(value) != auto else self.make_default("Rplcmnt")

	@Rplcmnt.deleter
	def Rplcmnt(self):
		del self._Rplcmnt
		self._Rplcmnt = None

	@property
	def Deltn(self):
		return self._Deltn

	@Deltn.setter
	def Deltn(self, value):
		self._Deltn = value if type(value) != auto else self.make_default("Deltn")

	@Deltn.deleter
	def Deltn(self):
		del self._Deltn
		self._Deltn = None

	@property
	def ElmtSeqNb(self):
		return self._ElmtSeqNb

	@ElmtSeqNb.setter
	def ElmtSeqNb(self, value):
		self._ElmtSeqNb = value if type(value) != auto else self.make_default("ElmtSeqNb")

	@ElmtSeqNb.deleter
	def ElmtSeqNb(self):
		del self._ElmtSeqNb
		self._ElmtSeqNb = None

	@property
	def Addtn(self):
		return self._Addtn

	@Addtn.setter
	def Addtn(self, value):
		self._Addtn = value if type(value) != auto else self.make_default("Addtn")

	@Addtn.deleter
	def Addtn(self):
		del self._Addtn
		self._Addtn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ElmtNm', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElmtPth', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rplcmnt', type=Replacement2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Deltn', type=Deletion2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ElmtSeqNb', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Addtn', type=Addition2, min=0, max=1, mutex_group=1, array=False),
	))

