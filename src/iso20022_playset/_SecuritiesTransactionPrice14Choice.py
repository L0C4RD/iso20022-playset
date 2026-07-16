# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BaseOneRate
from . import PercentageRate

class SecuritiesTransactionPrice14Choice(base_types._BaseFieldType):

	__slots__ = ["_Dcml", "_Rate"]
	@property
	def Dcml(self):
		return self._Dcml

	@Dcml.setter
	def Dcml(self, value):
		self._Dcml = value if value is not None else base_types.UninitialisedField(self, 'Dcml', BaseOneRate, False)

	@Dcml.deleter
	def Dcml(self):
		del self._Dcml
		self._Dcml = base_types.UninitialisedField(self, 'Dcml', BaseOneRate, False)

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', PercentageRate, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dcml', type=BaseOneRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
	))