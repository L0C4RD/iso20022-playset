import base_types
import ChargesPerTransaction5
import ChargesPerType5
import ChargesRecord11

class Charges5Choice(base_types._BaseFieldType):

	__slots__ = ["_PerTp", "_PerTx", "_Sngl"]
	@property
	def PerTp(self):
		return self._PerTp

	@PerTp.setter
	def PerTp(self, value):
		self._PerTp = value if type(value) != auto else self.make_default("PerTp")

	@PerTp.deleter
	def PerTp(self):
		del self._PerTp
		self._PerTp = None

	@property
	def PerTx(self):
		return self._PerTx

	@PerTx.setter
	def PerTx(self, value):
		self._PerTx = value if type(value) != auto else self.make_default("PerTx")

	@PerTx.deleter
	def PerTx(self):
		del self._PerTx
		self._PerTx = None

	@property
	def Sngl(self):
		return self._Sngl

	@Sngl.setter
	def Sngl(self, value):
		self._Sngl = value if type(value) != auto else self.make_default("Sngl")

	@Sngl.deleter
	def Sngl(self):
		del self._Sngl
		self._Sngl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PerTp', type=ChargesPerType5, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='PerTx', type=ChargesPerTransaction5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Sngl', type=ChargesRecord11, min=0, max=1, mutex_group=1, array=False),
	))

