# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Number
from . import PaymentTime3Code

class PaymentPeriod3(base_types._BaseFieldType):

	__slots__ = ["_Cd", "_NbOfDays"]
	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if value is not None else base_types.UninitialisedField(self, 'Cd', PaymentTime3Code, False)

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = base_types.UninitialisedField(self, 'Cd', PaymentTime3Code, False)

	@property
	def NbOfDays(self):
		return self._NbOfDays

	@NbOfDays.setter
	def NbOfDays(self, value):
		self._NbOfDays = value if value is not None else base_types.UninitialisedField(self, 'NbOfDays', Number, False)

	@NbOfDays.deleter
	def NbOfDays(self):
		del self._NbOfDays
		self._NbOfDays = base_types.UninitialisedField(self, 'NbOfDays', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cd', type=PaymentTime3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDays', type=Number, min=0, max=1, mutex_group=None, array=False),
	))