import base_types
import UpdateType35Choice
import SecurityAttributes12

class UpdateType36Choice(base_types._BaseFieldType):

	__slots__ = ["_Rplc", "_UpdTp"]
	@property
	def Rplc(self):
		return self._Rplc

	@Rplc.setter
	def Rplc(self, value):
		self._Rplc = value if type(value) != auto else self.make_default("Rplc")

	@Rplc.deleter
	def Rplc(self):
		del self._Rplc
		self._Rplc = None

	@property
	def UpdTp(self):
		return self._UpdTp

	@UpdTp.setter
	def UpdTp(self, value):
		self._UpdTp = value if type(value) != auto else self.make_default("UpdTp")

	@UpdTp.deleter
	def UpdTp(self):
		del self._UpdTp
		self._UpdTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rplc', type=SecurityAttributes12, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UpdTp', type=UpdateType35Choice, min=1, max=3, mutex_group=1, array=True),
	))

