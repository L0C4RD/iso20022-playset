import base_types
import Max350Text

class CorporateActionNarrative10(base_types._BaseFieldType):

	__slots__ = ["_AddtlTxt", "_PtyCtctNrrtv"]
	@property
	def AddtlTxt(self):
		return self._AddtlTxt

	@AddtlTxt.setter
	def AddtlTxt(self, value):
		self._AddtlTxt = value if type(value) != auto else self.make_default("AddtlTxt")

	@AddtlTxt.deleter
	def AddtlTxt(self):
		del self._AddtlTxt
		self._AddtlTxt = None

	@property
	def PtyCtctNrrtv(self):
		return self._PtyCtctNrrtv

	@PtyCtctNrrtv.setter
	def PtyCtctNrrtv(self, value):
		self._PtyCtctNrrtv = value if type(value) != auto else self.make_default("PtyCtctNrrtv")

	@PtyCtctNrrtv.deleter
	def PtyCtctNrrtv(self):
		del self._PtyCtctNrrtv
		self._PtyCtctNrrtv = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlTxt', type=Max350Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PtyCtctNrrtv', type=Max350Text, min=0, max=None, mutex_group=None, array=True),
	))

