# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification4
from . import ProductCategory1

class ProductCategory1Choice(base_types._BaseFieldType):

	__slots__ = ["_OthrPdctCtgy", "_StrdPdctCtgy"]
	@property
	def OthrPdctCtgy(self):
		return self._OthrPdctCtgy

	@OthrPdctCtgy.setter
	def OthrPdctCtgy(self, value):
		self._OthrPdctCtgy = value if value is not None else base_types.UninitialisedField(self, 'OthrPdctCtgy', GenericIdentification4, False)

	@OthrPdctCtgy.deleter
	def OthrPdctCtgy(self):
		del self._OthrPdctCtgy
		self._OthrPdctCtgy = base_types.UninitialisedField(self, 'OthrPdctCtgy', GenericIdentification4, False)

	@property
	def StrdPdctCtgy(self):
		return self._StrdPdctCtgy

	@StrdPdctCtgy.setter
	def StrdPdctCtgy(self, value):
		self._StrdPdctCtgy = value if value is not None else base_types.UninitialisedField(self, 'StrdPdctCtgy', ProductCategory1, False)

	@StrdPdctCtgy.deleter
	def StrdPdctCtgy(self):
		del self._StrdPdctCtgy
		self._StrdPdctCtgy = base_types.UninitialisedField(self, 'StrdPdctCtgy', ProductCategory1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrPdctCtgy', type=GenericIdentification4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StrdPdctCtgy', type=ProductCategory1, min=0, max=1, mutex_group=1, array=False),
	))