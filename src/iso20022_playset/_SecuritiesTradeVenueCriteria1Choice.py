# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AnyMIC1Code
from . import MICIdentifier

class SecuritiesTradeVenueCriteria1Choice(base_types._BaseFieldType):

	__slots__ = ["_AnyMIC", "_MIC"]
	@property
	def AnyMIC(self):
		return self._AnyMIC

	@AnyMIC.setter
	def AnyMIC(self, value):
		self._AnyMIC = value if value is not None else base_types.UninitialisedField(self, 'AnyMIC', AnyMIC1Code, False)

	@AnyMIC.deleter
	def AnyMIC(self):
		del self._AnyMIC
		self._AnyMIC = base_types.UninitialisedField(self, 'AnyMIC', AnyMIC1Code, False)

	@property
	def MIC(self):
		return self._MIC

	@MIC.setter
	def MIC(self, value):
		self._MIC = value if value is not None else base_types.UninitialisedField(self, 'MIC', MICIdentifier, True)

	@MIC.deleter
	def MIC(self):
		del self._MIC
		self._MIC = base_types.UninitialisedField(self, 'MIC', MICIdentifier, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AnyMIC', type=AnyMIC1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MIC', type=MICIdentifier, min=1, max=None, mutex_group=1, array=True),
	))