import base_types
import SignatureEnvelope
import Max140Text
import Number

class ApplicationSpecifics1(base_types._BaseFieldType):

	__slots__ = ["_SysUsr", "_TtlNbOfDocs", "_Sgntr"]
	@property
	def SysUsr(self):
		return self._SysUsr

	@SysUsr.setter
	def SysUsr(self, value):
		self._SysUsr = value if type(value) != auto else self.make_default("SysUsr")

	@SysUsr.deleter
	def SysUsr(self):
		del self._SysUsr
		self._SysUsr = None

	@property
	def TtlNbOfDocs(self):
		return self._TtlNbOfDocs

	@TtlNbOfDocs.setter
	def TtlNbOfDocs(self, value):
		self._TtlNbOfDocs = value if type(value) != auto else self.make_default("TtlNbOfDocs")

	@TtlNbOfDocs.deleter
	def TtlNbOfDocs(self):
		del self._TtlNbOfDocs
		self._TtlNbOfDocs = None

	@property
	def Sgntr(self):
		return self._Sgntr

	@Sgntr.setter
	def Sgntr(self, value):
		self._Sgntr = value if type(value) != auto else self.make_default("Sgntr")

	@Sgntr.deleter
	def Sgntr(self):
		del self._Sgntr
		self._Sgntr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SysUsr', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfDocs', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sgntr', type=SignatureEnvelope, min=0, max=1, mutex_group=None, array=False),
	))

