# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max100KBinary
from . import Max35Text

class BinaryFile1(base_types._BaseFieldType):

	__slots__ = ["_CharSet", "_InclBinryObjct", "_MIMETp", "_NcodgTp"]
	@property
	def CharSet(self):
		return self._CharSet

	@CharSet.setter
	def CharSet(self, value):
		self._CharSet = value if value is not None else base_types.UninitialisedField(self, 'CharSet', Max35Text, False)

	@CharSet.deleter
	def CharSet(self):
		del self._CharSet
		self._CharSet = base_types.UninitialisedField(self, 'CharSet', Max35Text, False)

	@property
	def InclBinryObjct(self):
		return self._InclBinryObjct

	@InclBinryObjct.setter
	def InclBinryObjct(self, value):
		self._InclBinryObjct = value if value is not None else base_types.UninitialisedField(self, 'InclBinryObjct', Max100KBinary, False)

	@InclBinryObjct.deleter
	def InclBinryObjct(self):
		del self._InclBinryObjct
		self._InclBinryObjct = base_types.UninitialisedField(self, 'InclBinryObjct', Max100KBinary, False)

	@property
	def MIMETp(self):
		return self._MIMETp

	@MIMETp.setter
	def MIMETp(self, value):
		self._MIMETp = value if value is not None else base_types.UninitialisedField(self, 'MIMETp', Max35Text, False)

	@MIMETp.deleter
	def MIMETp(self):
		del self._MIMETp
		self._MIMETp = base_types.UninitialisedField(self, 'MIMETp', Max35Text, False)

	@property
	def NcodgTp(self):
		return self._NcodgTp

	@NcodgTp.setter
	def NcodgTp(self, value):
		self._NcodgTp = value if value is not None else base_types.UninitialisedField(self, 'NcodgTp', Max35Text, False)

	@NcodgTp.deleter
	def NcodgTp(self):
		del self._NcodgTp
		self._NcodgTp = base_types.UninitialisedField(self, 'NcodgTp', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CharSet', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InclBinryObjct', type=Max100KBinary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MIMETp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcodgTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))