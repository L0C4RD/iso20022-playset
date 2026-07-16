# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max140Text
from . import OrderData3

class NewOrderReport2(base_types._BaseFieldType):

	__slots__ = ["_Ordr", "_RptId"]
	@property
	def Ordr(self):
		return self._Ordr

	@Ordr.setter
	def Ordr(self, value):
		self._Ordr = value if value is not None else base_types.UninitialisedField(self, 'Ordr', OrderData3, True)

	@Ordr.deleter
	def Ordr(self):
		del self._Ordr
		self._Ordr = base_types.UninitialisedField(self, 'Ordr', OrderData3, True)

	@property
	def RptId(self):
		return self._RptId

	@RptId.setter
	def RptId(self, value):
		self._RptId = value if value is not None else base_types.UninitialisedField(self, 'RptId', Max140Text, False)

	@RptId.deleter
	def RptId(self):
		del self._RptId
		self._RptId = base_types.UninitialisedField(self, 'RptId', Max140Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ordr', type=OrderData3, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptId', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
	))