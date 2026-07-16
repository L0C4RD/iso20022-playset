# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Exact3NumericText
from . import GenericIdentification36
from . import ISO20022MessageIdentificationText

class DocumentNumber5Choice(base_types._BaseFieldType):

	__slots__ = ["_LngNb", "_PrtryNb", "_ShrtNb"]
	@property
	def LngNb(self):
		return self._LngNb

	@LngNb.setter
	def LngNb(self, value):
		self._LngNb = value if value is not None else base_types.UninitialisedField(self, 'LngNb', ISO20022MessageIdentificationText, False)

	@LngNb.deleter
	def LngNb(self):
		del self._LngNb
		self._LngNb = base_types.UninitialisedField(self, 'LngNb', ISO20022MessageIdentificationText, False)

	@property
	def PrtryNb(self):
		return self._PrtryNb

	@PrtryNb.setter
	def PrtryNb(self, value):
		self._PrtryNb = value if value is not None else base_types.UninitialisedField(self, 'PrtryNb', GenericIdentification36, False)

	@PrtryNb.deleter
	def PrtryNb(self):
		del self._PrtryNb
		self._PrtryNb = base_types.UninitialisedField(self, 'PrtryNb', GenericIdentification36, False)

	@property
	def ShrtNb(self):
		return self._ShrtNb

	@ShrtNb.setter
	def ShrtNb(self, value):
		self._ShrtNb = value if value is not None else base_types.UninitialisedField(self, 'ShrtNb', Exact3NumericText, False)

	@ShrtNb.deleter
	def ShrtNb(self):
		del self._ShrtNb
		self._ShrtNb = base_types.UninitialisedField(self, 'ShrtNb', Exact3NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LngNb', type=ISO20022MessageIdentificationText, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryNb', type=GenericIdentification36, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ShrtNb', type=Exact3NumericText, min=0, max=1, mutex_group=1, array=False),
	))