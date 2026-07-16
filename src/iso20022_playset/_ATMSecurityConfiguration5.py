# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Number
from . import PINFormat4Code

class ATMSecurityConfiguration5(base_types._BaseFieldType):

	__slots__ = ["_PINFrmt", "_PINLngthCpblties"]
	@property
	def PINFrmt(self):
		return self._PINFrmt

	@PINFrmt.setter
	def PINFrmt(self, value):
		self._PINFrmt = value if value is not None else base_types.UninitialisedField(self, 'PINFrmt', PINFormat4Code, True)

	@PINFrmt.deleter
	def PINFrmt(self):
		del self._PINFrmt
		self._PINFrmt = base_types.UninitialisedField(self, 'PINFrmt', PINFormat4Code, True)

	@property
	def PINLngthCpblties(self):
		return self._PINLngthCpblties

	@PINLngthCpblties.setter
	def PINLngthCpblties(self, value):
		self._PINLngthCpblties = value if value is not None else base_types.UninitialisedField(self, 'PINLngthCpblties', Number, False)

	@PINLngthCpblties.deleter
	def PINLngthCpblties(self):
		del self._PINLngthCpblties
		self._PINLngthCpblties = base_types.UninitialisedField(self, 'PINLngthCpblties', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PINFrmt', type=PINFormat4Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PINLngthCpblties', type=Number, min=0, max=1, mutex_group=None, array=False),
	))