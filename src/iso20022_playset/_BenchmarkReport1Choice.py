# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BenchmarkCancellation1
from . import BenchmarkCreate1
from . import BenchmarkUpdate1

class BenchmarkReport1Choice(base_types._BaseFieldType):

	__slots__ = ["_Cret", "_Cxl", "_Upd"]
	@property
	def Cret(self):
		return self._Cret

	@Cret.setter
	def Cret(self, value):
		self._Cret = value if value is not None else base_types.UninitialisedField(self, 'Cret', BenchmarkCreate1, False)

	@Cret.deleter
	def Cret(self):
		del self._Cret
		self._Cret = base_types.UninitialisedField(self, 'Cret', BenchmarkCreate1, False)

	@property
	def Cxl(self):
		return self._Cxl

	@Cxl.setter
	def Cxl(self, value):
		self._Cxl = value if value is not None else base_types.UninitialisedField(self, 'Cxl', BenchmarkCancellation1, False)

	@Cxl.deleter
	def Cxl(self):
		del self._Cxl
		self._Cxl = base_types.UninitialisedField(self, 'Cxl', BenchmarkCancellation1, False)

	@property
	def Upd(self):
		return self._Upd

	@Upd.setter
	def Upd(self, value):
		self._Upd = value if value is not None else base_types.UninitialisedField(self, 'Upd', BenchmarkUpdate1, False)

	@Upd.deleter
	def Upd(self):
		del self._Upd
		self._Upd = base_types.UninitialisedField(self, 'Upd', BenchmarkUpdate1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cret', type=BenchmarkCreate1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cxl', type=BenchmarkCancellation1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Upd', type=BenchmarkUpdate1, min=0, max=1, mutex_group=1, array=False),
	))