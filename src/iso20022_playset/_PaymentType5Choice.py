# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max4AlphaNumericText
from . import PaymentType4Code

class PaymentType5Choice(base_types._BaseFieldType):

	__slots__ = ["_PrtryTp", "_Tp"]
	@property
	def PrtryTp(self):
		return self._PrtryTp

	@PrtryTp.setter
	def PrtryTp(self, value):
		self._PrtryTp = value if value is not None else base_types.UninitialisedField(self, 'PrtryTp', Max4AlphaNumericText, False)

	@PrtryTp.deleter
	def PrtryTp(self):
		del self._PrtryTp
		self._PrtryTp = base_types.UninitialisedField(self, 'PrtryTp', Max4AlphaNumericText, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', PaymentType4Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', PaymentType4Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtryTp', type=Max4AlphaNumericText, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Tp', type=PaymentType4Code, min=0, max=1, mutex_group=1, array=False),
	))