# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExternallyDefinedData5
from . import GenericIdentification176
from . import PositiveNumber

class PackageType5(base_types._BaseFieldType):

	__slots__ = ["_OffsetEnd", "_OffsetStart", "_PackgBlck", "_PackgId", "_PackgLngth"]
	@property
	def OffsetEnd(self):
		return self._OffsetEnd

	@OffsetEnd.setter
	def OffsetEnd(self, value):
		self._OffsetEnd = value if value is not None else base_types.UninitialisedField(self, 'OffsetEnd', PositiveNumber, False)

	@OffsetEnd.deleter
	def OffsetEnd(self):
		del self._OffsetEnd
		self._OffsetEnd = base_types.UninitialisedField(self, 'OffsetEnd', PositiveNumber, False)

	@property
	def OffsetStart(self):
		return self._OffsetStart

	@OffsetStart.setter
	def OffsetStart(self, value):
		self._OffsetStart = value if value is not None else base_types.UninitialisedField(self, 'OffsetStart', PositiveNumber, False)

	@OffsetStart.deleter
	def OffsetStart(self):
		del self._OffsetStart
		self._OffsetStart = base_types.UninitialisedField(self, 'OffsetStart', PositiveNumber, False)

	@property
	def PackgBlck(self):
		return self._PackgBlck

	@PackgBlck.setter
	def PackgBlck(self, value):
		self._PackgBlck = value if value is not None else base_types.UninitialisedField(self, 'PackgBlck', ExternallyDefinedData5, True)

	@PackgBlck.deleter
	def PackgBlck(self):
		del self._PackgBlck
		self._PackgBlck = base_types.UninitialisedField(self, 'PackgBlck', ExternallyDefinedData5, True)

	@property
	def PackgId(self):
		return self._PackgId

	@PackgId.setter
	def PackgId(self, value):
		self._PackgId = value if value is not None else base_types.UninitialisedField(self, 'PackgId', GenericIdentification176, False)

	@PackgId.deleter
	def PackgId(self):
		del self._PackgId
		self._PackgId = base_types.UninitialisedField(self, 'PackgId', GenericIdentification176, False)

	@property
	def PackgLngth(self):
		return self._PackgLngth

	@PackgLngth.setter
	def PackgLngth(self, value):
		self._PackgLngth = value if value is not None else base_types.UninitialisedField(self, 'PackgLngth', PositiveNumber, False)

	@PackgLngth.deleter
	def PackgLngth(self):
		del self._PackgLngth
		self._PackgLngth = base_types.UninitialisedField(self, 'PackgLngth', PositiveNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OffsetEnd', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffsetStart', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PackgBlck', type=ExternallyDefinedData5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PackgId', type=GenericIdentification176, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PackgLngth', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
	))