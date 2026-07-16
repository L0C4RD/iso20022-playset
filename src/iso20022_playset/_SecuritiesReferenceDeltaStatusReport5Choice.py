# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesReferenceDataReport6
from . import SecuritiesReferenceDataReport7

class SecuritiesReferenceDeltaStatusReport5Choice(base_types._BaseFieldType):

	__slots__ = ["_CancRcrd", "_ModfdRcrd", "_NewRcrd", "_TermntdRcrd"]
	@property
	def CancRcrd(self):
		return self._CancRcrd

	@CancRcrd.setter
	def CancRcrd(self, value):
		self._CancRcrd = value if value is not None else base_types.UninitialisedField(self, 'CancRcrd', SecuritiesReferenceDataReport7, False)

	@CancRcrd.deleter
	def CancRcrd(self):
		del self._CancRcrd
		self._CancRcrd = base_types.UninitialisedField(self, 'CancRcrd', SecuritiesReferenceDataReport7, False)

	@property
	def ModfdRcrd(self):
		return self._ModfdRcrd

	@ModfdRcrd.setter
	def ModfdRcrd(self, value):
		self._ModfdRcrd = value if value is not None else base_types.UninitialisedField(self, 'ModfdRcrd', SecuritiesReferenceDataReport6, False)

	@ModfdRcrd.deleter
	def ModfdRcrd(self):
		del self._ModfdRcrd
		self._ModfdRcrd = base_types.UninitialisedField(self, 'ModfdRcrd', SecuritiesReferenceDataReport6, False)

	@property
	def NewRcrd(self):
		return self._NewRcrd

	@NewRcrd.setter
	def NewRcrd(self, value):
		self._NewRcrd = value if value is not None else base_types.UninitialisedField(self, 'NewRcrd', SecuritiesReferenceDataReport6, False)

	@NewRcrd.deleter
	def NewRcrd(self):
		del self._NewRcrd
		self._NewRcrd = base_types.UninitialisedField(self, 'NewRcrd', SecuritiesReferenceDataReport6, False)

	@property
	def TermntdRcrd(self):
		return self._TermntdRcrd

	@TermntdRcrd.setter
	def TermntdRcrd(self, value):
		self._TermntdRcrd = value if value is not None else base_types.UninitialisedField(self, 'TermntdRcrd', SecuritiesReferenceDataReport6, False)

	@TermntdRcrd.deleter
	def TermntdRcrd(self):
		del self._TermntdRcrd
		self._TermntdRcrd = base_types.UninitialisedField(self, 'TermntdRcrd', SecuritiesReferenceDataReport6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CancRcrd', type=SecuritiesReferenceDataReport7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ModfdRcrd', type=SecuritiesReferenceDataReport6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NewRcrd', type=SecuritiesReferenceDataReport6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TermntdRcrd', type=SecuritiesReferenceDataReport6, min=0, max=1, mutex_group=1, array=False),
	))