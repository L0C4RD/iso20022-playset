# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import OptionMultipleBarrierLevels1
from . import SecuritiesTransactionPrice23Choice

class OptionBarrierLevel1Choice(base_types._BaseFieldType):

	__slots__ = ["_Mltpl", "_Sngl"]
	@property
	def Mltpl(self):
		return self._Mltpl

	@Mltpl.setter
	def Mltpl(self, value):
		self._Mltpl = value if value is not None else base_types.UninitialisedField(self, 'Mltpl', OptionMultipleBarrierLevels1, False)

	@Mltpl.deleter
	def Mltpl(self):
		del self._Mltpl
		self._Mltpl = base_types.UninitialisedField(self, 'Mltpl', OptionMultipleBarrierLevels1, False)

	@property
	def Sngl(self):
		return self._Sngl

	@Sngl.setter
	def Sngl(self, value):
		self._Sngl = value if value is not None else base_types.UninitialisedField(self, 'Sngl', SecuritiesTransactionPrice23Choice, False)

	@Sngl.deleter
	def Sngl(self):
		del self._Sngl
		self._Sngl = base_types.UninitialisedField(self, 'Sngl', SecuritiesTransactionPrice23Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Mltpl', type=OptionMultipleBarrierLevels1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Sngl', type=SecuritiesTransactionPrice23Choice, min=0, max=1, mutex_group=1, array=False),
	))