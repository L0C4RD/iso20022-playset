# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max140Text
from . import Number
from . import SignatureEnvelope

class ApplicationSpecifics1(base_types._BaseFieldType):

	__slots__ = ["_Sgntr", "_SysUsr", "_TtlNbOfDocs"]
	@property
	def Sgntr(self):
		return self._Sgntr

	@Sgntr.setter
	def Sgntr(self, value):
		self._Sgntr = value if value is not None else base_types.UninitialisedField(self, 'Sgntr', SignatureEnvelope, False)

	@Sgntr.deleter
	def Sgntr(self):
		del self._Sgntr
		self._Sgntr = base_types.UninitialisedField(self, 'Sgntr', SignatureEnvelope, False)

	@property
	def SysUsr(self):
		return self._SysUsr

	@SysUsr.setter
	def SysUsr(self, value):
		self._SysUsr = value if value is not None else base_types.UninitialisedField(self, 'SysUsr', Max140Text, False)

	@SysUsr.deleter
	def SysUsr(self):
		del self._SysUsr
		self._SysUsr = base_types.UninitialisedField(self, 'SysUsr', Max140Text, False)

	@property
	def TtlNbOfDocs(self):
		return self._TtlNbOfDocs

	@TtlNbOfDocs.setter
	def TtlNbOfDocs(self, value):
		self._TtlNbOfDocs = value if value is not None else base_types.UninitialisedField(self, 'TtlNbOfDocs', Number, False)

	@TtlNbOfDocs.deleter
	def TtlNbOfDocs(self):
		del self._TtlNbOfDocs
		self._TtlNbOfDocs = base_types.UninitialisedField(self, 'TtlNbOfDocs', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sgntr', type=SignatureEnvelope, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysUsr', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfDocs', type=Number, min=1, max=1, mutex_group=None, array=False),
	))