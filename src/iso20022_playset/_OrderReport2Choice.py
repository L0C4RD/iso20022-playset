# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CancelOrderReport1
from . import NewOrderReport2

class OrderReport2Choice(base_types._BaseFieldType):

	__slots__ = ["_Cxl", "_New"]
	@property
	def Cxl(self):
		return self._Cxl

	@Cxl.setter
	def Cxl(self, value):
		self._Cxl = value if value is not None else base_types.UninitialisedField(self, 'Cxl', CancelOrderReport1, False)

	@Cxl.deleter
	def Cxl(self):
		del self._Cxl
		self._Cxl = base_types.UninitialisedField(self, 'Cxl', CancelOrderReport1, False)

	@property
	def New(self):
		return self._New

	@New.setter
	def New(self, value):
		self._New = value if value is not None else base_types.UninitialisedField(self, 'New', NewOrderReport2, False)

	@New.deleter
	def New(self):
		del self._New
		self._New = base_types.UninitialisedField(self, 'New', NewOrderReport2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cxl', type=CancelOrderReport1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='New', type=NewOrderReport2, min=0, max=1, mutex_group=1, array=False),
	))