import base_types
import OptionMultipleBarrierLevels1
import SecuritiesTransactionPrice23Choice

class OptionBarrierLevel1Choice(base_types._BaseFieldType):

	__slots__ = ["_Mltpl", "_Sngl"]
	@property
	def Mltpl(self):
		return self._Mltpl

	@Mltpl.setter
	def Mltpl(self, value):
		self._Mltpl = value if type(value) != auto else self.make_default("Mltpl")

	@Mltpl.deleter
	def Mltpl(self):
		del self._Mltpl
		self._Mltpl = None

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
		base_types.FieldEntry(name='Mltpl', type=OptionMultipleBarrierLevels1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Sngl', type=SecuritiesTransactionPrice23Choice, min=0, max=1, mutex_group=1, array=False),
	))

