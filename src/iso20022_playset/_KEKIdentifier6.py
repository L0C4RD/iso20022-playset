# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max140Text
from . import Min5Max16Binary
from . import Number

class KEKIdentifier6(base_types._BaseFieldType):

	__slots__ = ["_DerivtnId", "_KeyId", "_KeyVrsn", "_SeqNb"]
	@property
	def DerivtnId(self):
		return self._DerivtnId

	@DerivtnId.setter
	def DerivtnId(self, value):
		self._DerivtnId = value if value is not None else base_types.UninitialisedField(self, 'DerivtnId', Min5Max16Binary, False)

	@DerivtnId.deleter
	def DerivtnId(self):
		del self._DerivtnId
		self._DerivtnId = base_types.UninitialisedField(self, 'DerivtnId', Min5Max16Binary, False)

	@property
	def KeyId(self):
		return self._KeyId

	@KeyId.setter
	def KeyId(self, value):
		self._KeyId = value if value is not None else base_types.UninitialisedField(self, 'KeyId', Max140Text, False)

	@KeyId.deleter
	def KeyId(self):
		del self._KeyId
		self._KeyId = base_types.UninitialisedField(self, 'KeyId', Max140Text, False)

	@property
	def KeyVrsn(self):
		return self._KeyVrsn

	@KeyVrsn.setter
	def KeyVrsn(self, value):
		self._KeyVrsn = value if value is not None else base_types.UninitialisedField(self, 'KeyVrsn', Max140Text, False)

	@KeyVrsn.deleter
	def KeyVrsn(self):
		del self._KeyVrsn
		self._KeyVrsn = base_types.UninitialisedField(self, 'KeyVrsn', Max140Text, False)

	@property
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if value is not None else base_types.UninitialisedField(self, 'SeqNb', Number, False)

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = base_types.UninitialisedField(self, 'SeqNb', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DerivtnId', type=Min5Max16Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyId', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyVrsn', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNb', type=Number, min=0, max=1, mutex_group=None, array=False),
	))