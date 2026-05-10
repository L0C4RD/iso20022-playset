from . import base_types
from ._Max100KBinary import Max100KBinary
from ._Max35Text import Max35Text

class BinaryFile1(base_types._BaseFieldType):

	__slots__ = ["_CharSet", "_InclBinryObjct", "_MIMETp", "_NcodgTp"]
	@property
	def CharSet(self):
		return self._CharSet

	@CharSet.setter
	def CharSet(self, value):
		self._CharSet = value if type(value) != base_types.auto else self.make_default("CharSet")

	@CharSet.deleter
	def CharSet(self):
		del self._CharSet
		self._CharSet = None

	@property
	def InclBinryObjct(self):
		return self._InclBinryObjct

	@InclBinryObjct.setter
	def InclBinryObjct(self, value):
		self._InclBinryObjct = value if type(value) != base_types.auto else self.make_default("InclBinryObjct")

	@InclBinryObjct.deleter
	def InclBinryObjct(self):
		del self._InclBinryObjct
		self._InclBinryObjct = None

	@property
	def MIMETp(self):
		return self._MIMETp

	@MIMETp.setter
	def MIMETp(self, value):
		self._MIMETp = value if type(value) != base_types.auto else self.make_default("MIMETp")

	@MIMETp.deleter
	def MIMETp(self):
		del self._MIMETp
		self._MIMETp = None

	@property
	def NcodgTp(self):
		return self._NcodgTp

	@NcodgTp.setter
	def NcodgTp(self, value):
		self._NcodgTp = value if type(value) != base_types.auto else self.make_default("NcodgTp")

	@NcodgTp.deleter
	def NcodgTp(self):
		del self._NcodgTp
		self._NcodgTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CharSet', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InclBinryObjct', type=Max100KBinary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MIMETp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcodgTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

