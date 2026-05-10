from . import base_types
import CancellationReason32Choice
import Max35Text

class InvestmentFundOrder9(base_types._BaseFieldType):

	__slots__ = ["_OrdrRef", "_CxlRef", "_ClntRef", "_CxlRsn"]
	@property
	def OrdrRef(self):
		return self._OrdrRef

	@OrdrRef.setter
	def OrdrRef(self, value):
		self._OrdrRef = value if type(value) != auto else self.make_default("OrdrRef")

	@OrdrRef.deleter
	def OrdrRef(self):
		del self._OrdrRef
		self._OrdrRef = None

	@property
	def CxlRef(self):
		return self._CxlRef

	@CxlRef.setter
	def CxlRef(self, value):
		self._CxlRef = value if type(value) != auto else self.make_default("CxlRef")

	@CxlRef.deleter
	def CxlRef(self):
		del self._CxlRef
		self._CxlRef = None

	@property
	def ClntRef(self):
		return self._ClntRef

	@ClntRef.setter
	def ClntRef(self, value):
		self._ClntRef = value if type(value) != auto else self.make_default("ClntRef")

	@ClntRef.deleter
	def ClntRef(self):
		del self._ClntRef
		self._ClntRef = None

	@property
	def CxlRsn(self):
		return self._CxlRsn

	@CxlRsn.setter
	def CxlRsn(self, value):
		self._CxlRsn = value if type(value) != auto else self.make_default("CxlRsn")

	@CxlRsn.deleter
	def CxlRsn(self):
		del self._CxlRsn
		self._CxlRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrdrRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRsn', type=CancellationReason32Choice, min=0, max=1, mutex_group=None, array=False),
	))

