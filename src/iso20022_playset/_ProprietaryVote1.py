# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification30
from . import QuantityOrCode1Choice

class ProprietaryVote1(base_types._BaseFieldType):

	__slots__ = ["_Cd", "_Qty"]
	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if value is not None else base_types.UninitialisedField(self, 'Cd', GenericIdentification30, False)

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = base_types.UninitialisedField(self, 'Cd', GenericIdentification30, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', QuantityOrCode1Choice, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', QuantityOrCode1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cd', type=GenericIdentification30, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=QuantityOrCode1Choice, min=1, max=1, mutex_group=None, array=False),
	))