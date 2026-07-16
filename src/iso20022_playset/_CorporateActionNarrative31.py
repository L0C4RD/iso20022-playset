# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max350Text

class CorporateActionNarrative31(base_types._BaseFieldType):

	__slots__ = ["_AddtlTxt", "_NrrtvVrsn", "_PtyCtctNrrtv", "_TaxtnConds"]
	@property
	def AddtlTxt(self):
		return self._AddtlTxt

	@AddtlTxt.setter
	def AddtlTxt(self, value):
		self._AddtlTxt = value if value is not None else base_types.UninitialisedField(self, 'AddtlTxt', Max350Text, True)

	@AddtlTxt.deleter
	def AddtlTxt(self):
		del self._AddtlTxt
		self._AddtlTxt = base_types.UninitialisedField(self, 'AddtlTxt', Max350Text, True)

	@property
	def NrrtvVrsn(self):
		return self._NrrtvVrsn

	@NrrtvVrsn.setter
	def NrrtvVrsn(self, value):
		self._NrrtvVrsn = value if value is not None else base_types.UninitialisedField(self, 'NrrtvVrsn', Max350Text, True)

	@NrrtvVrsn.deleter
	def NrrtvVrsn(self):
		del self._NrrtvVrsn
		self._NrrtvVrsn = base_types.UninitialisedField(self, 'NrrtvVrsn', Max350Text, True)

	@property
	def PtyCtctNrrtv(self):
		return self._PtyCtctNrrtv

	@PtyCtctNrrtv.setter
	def PtyCtctNrrtv(self, value):
		self._PtyCtctNrrtv = value if value is not None else base_types.UninitialisedField(self, 'PtyCtctNrrtv', Max350Text, True)

	@PtyCtctNrrtv.deleter
	def PtyCtctNrrtv(self):
		del self._PtyCtctNrrtv
		self._PtyCtctNrrtv = base_types.UninitialisedField(self, 'PtyCtctNrrtv', Max350Text, True)

	@property
	def TaxtnConds(self):
		return self._TaxtnConds

	@TaxtnConds.setter
	def TaxtnConds(self, value):
		self._TaxtnConds = value if value is not None else base_types.UninitialisedField(self, 'TaxtnConds', Max350Text, True)

	@TaxtnConds.deleter
	def TaxtnConds(self):
		del self._TaxtnConds
		self._TaxtnConds = base_types.UninitialisedField(self, 'TaxtnConds', Max350Text, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlTxt', type=Max350Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NrrtvVrsn', type=Max350Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PtyCtctNrrtv', type=Max350Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxtnConds', type=Max350Text, min=0, max=None, mutex_group=None, array=True),
	))